+++
title = "What is random generation?"
date = "2026-05-06"
[taxonomies]
tags = ['testing']
language = ["en"]
+++

I wanted to write this as a sequel to
["What is a property?"](http://alperenkeles.com/posts/what-is-a-property/) where I would
talk about how Property-Based Testing libraries generate random structures, don't worry,
I'll still do that! But I realized that without talking about randomness in computers,
the writing would be incomplete. So the first part of this article will go into a core
problem that we consider "solved" in PBT, which is designing good random number
generators, with the latter part talking about implementing complex random data
generators on top of such RNGs.

## Random Number Generation in Computers

Randomness is a noisy topic. At a first approximation, it signifies uncertainty, or
orderlessness, or more formally, high entropy. Of course, in computer programs, random
generation is fake; we use PRNGs (pseudo-random number generators), high-entropy
functions of which the relationship between the seed and the generated random number is
as arbitrary as possible. A very simple example of a PRNG is a
[linear congruential generator (LCG)](https://en.wikipedia.org/wiki/Linear_congruential_generator):

```ts
function lcg(seed: number): () => number {
  const a = 1664525;
  const c = 1013904223;
  const m = 2 ** 32;
  let state = seed;
  return () => {
    state = (a * state + c) % m;
    return state;
  };
}

const rand = lcg(42);
rand(); // 1083814273
rand(); // 380859148
rand(); // 2338846736
```

The randomness of the out of an LCG depends on its parameter choices, for instance
`a = 1` and `c = 1` results in a counter module `m`. Precursor of LCG (according to
Wikipedia) is apparently a
[Lehmer random number generator](https://en.wikipedia.org/wiki/Lehmer_random_number_generator)
where `c = 0`, `m` is either a prime, or a power of a prime number; the initial seed
must be a [coprime](https://en.wikipedia.org/wiki/Coprime_integers) of `m`, and `a` must
be "an element of high multiplicative order modulo m". As I've said, I'm also learning
about random number generation as I write this post, so I created a visualization. There
are some presets, and you can also try other numbers if you would like.

### Visualizing LCG quality

Pick a preset or tweak the parameters and watch what `a`, `c`, and `m` do to the output.
The left panel plots consecutive triples `(xₙ, xₙ₊₁, xₙ₊₂)` (or pairs `(xₙ, xₙ₊₁)` if
you switch the view) — if visible structure shows up there, the generator is leaking
patterns the spectral test would catch. The right panel is a histogram over `[0, 1]`,
which tells you whether the output is at least uniform on the surface.

<div class="lcg-demo">
  <div class="lcg-row">
    <label>a <input id="lcg-a" type="number" value="1664525"></label>
    <label>c <input id="lcg-c" type="number" value="1013904223"></label>
    <label>m <input id="lcg-m" type="number" value="4294967296"></label>
    <label>seed <input id="lcg-seed" type="number" value="42"></label>
    <label>samples <input id="lcg-n" type="number" value="20000"></label>
  </div>
  <div class="lcg-row lcg-presets">
    <button class="lcg-preset" data-a="1664525" data-c="1013904223" data-m="4294967296" data-seed="42" data-n="20000">Numerical Recipes (good)</button>
    <button class="lcg-preset" data-a="65539" data-c="0" data-m="2147483648" data-seed="1" data-n="20000">RANDU (problematic)</button>
    <button class="lcg-preset" data-a="48271" data-c="0" data-m="2147483647" data-seed="1" data-n="20000">MINSTD / Lehmer</button>
    <button class="lcg-preset" data-a="1" data-c="1" data-m="100" data-seed="0" data-n="300">Counter (a=1, c=1)</button>
    <button class="lcg-preset" data-a="9" data-c="3" data-m="32" data-seed="0" data-n="300">Toy (tiny m)</button>
    <button class="lcg-preset" data-a="11" data-c="0" data-m="63" data-seed="1" data-n="300">Lehmer, weak period</button>
  </div>
  <div class="lcg-row lcg-charts">
    <figure>
      <canvas id="lcg-scatter" width="320" height="320"></canvas>
      <figcaption>
        <select id="lcg-view">
          <option value="3d" selected>3D triples (xₙ, xₙ₊₁, xₙ₊₂), rotating</option>
          <option value="2d">2D pairs (xₙ, xₙ₊₁)</option>
        </select>
        <br>patterns here mean weak randomness — try RANDU in 3D
      </figcaption>
    </figure>
    <figure>
      <canvas id="lcg-hist" width="320" height="200"></canvas>
      <figcaption>distribution over [0, 1]</figcaption>
    </figure>
  </div>
  <p id="lcg-info"></p>
</div>

<style>
  .lcg-demo { border: 1px solid rgba(127, 127, 127, 0.35); padding: 1em; margin: 1.25em 0; border-radius: 6px; }
  .lcg-row { display: flex; flex-wrap: wrap; gap: 0.5em 0.75em; align-items: center; margin-bottom: 0.75em; }
  .lcg-demo label { display: inline-flex; gap: 0.35em; align-items: center; font-size: 0.9em; }
  .lcg-demo input[type=number] { width: 8.5em; padding: 0.2em 0.4em; font-family: inherit; }
  .lcg-demo button { padding: 0.3em 0.6em; cursor: pointer; font-size: 0.85em; }
  .lcg-charts { gap: 1.5em; align-items: flex-start; }
  .lcg-demo figure { margin: 0; text-align: center; }
  .lcg-demo figcaption { font-size: 0.8em; opacity: 0.75; margin-top: 0.35em; }
  .lcg-demo canvas { background: rgba(127, 127, 127, 0.06); display: block; max-width: 100%; height: auto; }
  #lcg-info { font-size: 0.85em; opacity: 0.85; margin: 0; font-family: monospace; }
</style>

<script>
(function () {
  const $ = (id) => document.getElementById(id);
  const scatter = $('lcg-scatter').getContext('2d');
  const hist = $('lcg-hist').getContext('2d');

  function generate(a, c, m, seed, n) {
    const out = new Float64Array(n);
    const A = BigInt(a), C = BigInt(c), M = BigInt(m);
    if (M <= 0n) return out;
    let s = ((BigInt(seed) % M) + M) % M;
    const Mn = Number(M);
    for (let i = 0; i < n; i++) {
      s = (A * s + C) % M;
      out[i] = Number(s) / Mn;
    }
    return out;
  }

  function drawScatter2D(xs) {
    const w = scatter.canvas.width, h = scatter.canvas.height;
    scatter.clearRect(0, 0, w, h);
    scatter.fillStyle = 'rgba(127, 127, 127, 0.06)';
    scatter.fillRect(0, 0, w, h);
    scatter.fillStyle = '#41C9E2';
    const pad = 3;
    for (let i = 0; i < xs.length - 1; i++) {
      const px = xs[i] * (w - pad * 2) + pad;
      const py = (1 - xs[i + 1]) * (h - pad * 2) + pad;
      scatter.fillRect(px, py, 2, 2);
    }
  }

  function drawScatter3D(xs, angle) {
    const w = scatter.canvas.width, h = scatter.canvas.height;
    scatter.clearRect(0, 0, w, h);
    scatter.fillStyle = 'rgba(127, 127, 127, 0.06)';
    scatter.fillRect(0, 0, w, h);
    const cx = w / 2, cy = h / 2;
    const scale = Math.min(w, h) * 0.42;
    const cosT = Math.cos(angle), sinT = Math.sin(angle);
    const tilt = 0.45;
    const cosP = Math.cos(tilt), sinP = Math.sin(tilt);
    scatter.fillStyle = '#41C9E2';
    for (let i = 0; i < xs.length - 2; i++) {
      const x = xs[i] - 0.5;
      const y = xs[i + 1] - 0.5;
      const z = xs[i + 2] - 0.5;
      const x1 = x * cosT + z * sinT;
      const z1 = -x * sinT + z * cosT;
      const y1 = y * cosP - z1 * sinP;
      const px = cx + x1 * scale;
      const py = cy - y1 * scale;
      scatter.fillRect(px, py, 2, 2);
    }
    scatter.strokeStyle = 'rgba(127, 127, 127, 0.4)';
    scatter.lineWidth = 1;
    const corners = [
      [-0.5, -0.5, -0.5], [0.5, -0.5, -0.5], [0.5, 0.5, -0.5], [-0.5, 0.5, -0.5],
      [-0.5, -0.5, 0.5], [0.5, -0.5, 0.5], [0.5, 0.5, 0.5], [-0.5, 0.5, 0.5],
    ].map(([x, y, z]) => {
      const x1 = x * cosT + z * sinT;
      const z1 = -x * sinT + z * cosT;
      const y1 = y * cosP - z1 * sinP;
      return [cx + x1 * scale, cy - y1 * scale];
    });
    const edges = [[0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[0,4],[1,5],[2,6],[3,7]];
    scatter.beginPath();
    for (const [a, b] of edges) {
      scatter.moveTo(corners[a][0], corners[a][1]);
      scatter.lineTo(corners[b][0], corners[b][1]);
    }
    scatter.stroke();
  }

  let viewMode = '3d';
  let lastSamples = null;
  let rafId = null;
  let angle = 0;

  function stopAnim() {
    if (rafId !== null) { cancelAnimationFrame(rafId); rafId = null; }
  }

  function startAnim() {
    stopAnim();
    function loop() {
      if (viewMode !== '3d' || !lastSamples) { rafId = null; return; }
      drawScatter3D(lastSamples, angle);
      angle += 0.006;
      rafId = requestAnimationFrame(loop);
    }
    rafId = requestAnimationFrame(loop);
  }

  function drawScatter(xs) {
    if (viewMode === '3d') {
      drawScatter3D(xs, angle);
      startAnim();
    } else {
      stopAnim();
      drawScatter2D(xs);
    }
  }

  function drawHist(xs) {
    const w = hist.canvas.width, h = hist.canvas.height;
    const bins = 40;
    const counts = new Uint32Array(bins);
    for (let i = 0; i < xs.length; i++) {
      const b = Math.min(bins - 1, Math.floor(xs[i] * bins));
      counts[b]++;
    }
    const expected = xs.length / bins;
    let maxC = 0;
    for (let i = 0; i < bins; i++) if (counts[i] > maxC) maxC = counts[i];
    const scaleMax = Math.max(maxC, expected * 2);
    hist.clearRect(0, 0, w, h);
    hist.fillStyle = 'rgba(127, 127, 127, 0.06)';
    hist.fillRect(0, 0, w, h);
    const bw = w / bins;
    const usable = h - 10;
    hist.fillStyle = '#D862BC';
    for (let i = 0; i < bins; i++) {
      const bh = scaleMax > 0 ? (counts[i] / scaleMax) * usable : 0;
      hist.fillRect(i * bw + 0.5, h - bh, bw - 1, bh);
    }
    if (scaleMax > 0) {
      const yExpected = h - (expected / scaleMax) * usable;
      hist.strokeStyle = 'rgba(127, 127, 127, 0.85)';
      hist.lineWidth = 1;
      hist.setLineDash([4, 3]);
      hist.beginPath();
      hist.moveTo(0, yExpected);
      hist.lineTo(w, yExpected);
      hist.stroke();
      hist.setLineDash([]);
      hist.fillStyle = 'rgba(127, 127, 127, 0.95)';
      hist.font = '10px monospace';
      hist.textBaseline = 'bottom';
      hist.fillText(`expected ≈ ${expected.toFixed(0)}`, 4, yExpected - 2);
    }
  }

  function detectPeriod(a, c, m, seed, cap) {
    const A = BigInt(a), C = BigInt(c), M = BigInt(m);
    if (M <= 0n) return null;
    let s = ((BigInt(seed) % M) + M) % M;
    const seen = new Map();
    for (let i = 0; i < cap; i++) {
      const key = s.toString();
      if (seen.has(key)) return i - seen.get(key);
      seen.set(key, i);
      s = (A * s + C) % M;
    }
    return null;
  }

  function chiSquare(xs, bins) {
    const counts = new Uint32Array(bins);
    for (let i = 0; i < xs.length; i++) {
      const b = Math.min(bins - 1, Math.floor(xs[i] * bins));
      counts[b]++;
    }
    const expected = xs.length / bins;
    let chi = 0;
    for (let i = 0; i < bins; i++) chi += (counts[i] - expected) ** 2 / expected;
    return chi;
  }

  function refresh() {
    const a = Number($('lcg-a').value);
    const c = Number($('lcg-c').value);
    const m = Number($('lcg-m').value);
    const seed = Number($('lcg-seed').value);
    const n = Math.max(2, Math.min(50000, Number($('lcg-n').value) || 0));
    if (!Number.isFinite(a) || !Number.isFinite(c) || !Number.isFinite(m) || m <= 0) {
      $('lcg-info').textContent = 'enter valid integers (m must be > 0)';
      return;
    }
    const xs = generate(a, c, m, seed, n);
    lastSamples = xs;
    drawScatter(xs);
    drawHist(xs);
    const period = m <= 200000 ? detectPeriod(a, c, m, seed, Math.min(m + 2, 400000)) : null;
    const chi = chiSquare(xs, 40).toFixed(2);
    const periodTxt = period !== null
      ? `period = ${period}`
      : (m <= 200000 ? 'no period in scan' : 'period not scanned (m large)');
    $('lcg-info').textContent = `${n} samples · ${periodTxt} · chi² (40 bins) ≈ ${chi} (expected ≈ 39 for uniform)`;
  }

  document.querySelectorAll('.lcg-preset').forEach((btn) => {
    btn.addEventListener('click', () => {
      $('lcg-a').value = btn.dataset.a;
      $('lcg-c').value = btn.dataset.c;
      $('lcg-m').value = btn.dataset.m;
      $('lcg-seed').value = btn.dataset.seed;
      $('lcg-n').value = btn.dataset.n;
      refresh();
    });
  });

  ['lcg-a', 'lcg-c', 'lcg-m', 'lcg-seed', 'lcg-n'].forEach((id) => {
    $(id).addEventListener('input', refresh);
  });

  $('lcg-view').addEventListener('change', (e) => {
    viewMode = e.target.value;
    if (lastSamples) drawScatter(lastSamples);
  });

  refresh();
})();
</script>

There are a whole sequence of random number generators, there are new ones
[right up to 2023](<https://en.wikipedia.org/wiki/List_of_random_number_generators#Pseudorandom_number_generators_(PRNGs)>),
it's an active area of research of which we frequently use its results, many of the
algorithms show up on the random generation libraries and standart libraries of many
PLs.

Of course, the discussion is incomplete with the famous lava lambs!

![CF Lava Lambs](./image.png)

Once we have an algorithm that can take an arbitrary seed and produce a high-entropy
random number out of it, we want a high-entropy source of those seeds too. For
Cloudflare, it's apparently their pattern-absent lava lambs; for many of us, it's the OS
source of randomness [`/dev/urandom`](https://en.wikipedia.org/wiki//dev/random) that
uses the only real source of randomness for a computer, the physical world, to produce
seeds.

Armed with true randomness and well-designed algorithms, we can generate uniform random
64 bit numbers, so are we done? Well, the issue is, we really don't wanna generate 64
bit numbers, do we? We want to generate booleans, floats, bounded numbers, collections,
complex structures... We also don't want uniform randomness per se, we wanna be able to
bias the random generator if needed, perhaps to fit into certain other distributions;
luckily, we can build all of this from our simple primitive 64 random bits.

### Generating Floats

Random floating-point numbers typically generated via generating a random float in the
interval [0.0, 1.0), and scaling the number based on the range. Nima Badizadegan has a
much better [article](https://specbranch.com/posts/fp-rand/) on random fp generation, so
I'll just give the gist here, the following is from the Haskell
[random](https://github.com/haskell/random/blob/master/src/System/Random/Internal.hs#L1443-L1449)
library:

```haskell
-- | Generates uniformly distributed 'Double' in the range \([0, 1]\).
--   Numbers are generated by generating uniform 'Word64' and dividing
--   it by \(2^{64}\). It's used to implement 'UniformRange' instance for
--   'Double'.
--
-- @since 1.2.0
uniformDouble01M :: forall g m. StatefulGen g m => g -> m Double
uniformDouble01M g = do
  w64 <- uniformWord64 g
  return $ fromIntegral w64 / m
  where
    m = fromIntegral (maxBound :: Word64) :: Double
```

Essentially, we generate a random 64 bit integer, divide it by the largest 64 bit
integer possible in the domain of the floating point numbers:

```ts
function randomFloat(): number {
  return rand() / 2 ** 64;
}
```

If we have a different range, we can just scale up [0, 1) to [a, b):

```ts
function randomFloatInRange(a: number, b: number): number {
  return a + (b - a) * randomFloat();
}
```

### Generating Booleans

Generating a uniform random boolean is easy, `rand` gives us 64 random bits, we can just
check any one of them;

```ts
function randomBoolean(): boolean {
  return (rand() & 1) === 0;
}
```

but do you have the courage to generate biased booleans? That is where we can rely on
the random float generation:

```ts
function randomBiasedBoolean(p: number): boolean {
  return randomFloat() < p;
}
```

### Generating Bounded Integers

We can easily model `randomInt(a, b)` as `a + randomInt(0, b - a)`, so we can focus on
solving random generation for `[0, a)`. A simple approximation is `rand() % a`, with a
classic problem, bias. When `a` is not a power of 2, then there is a part of the
interval that'll be hit a little bit more because the bins (`k % a`) will not have the
same number of elements, let's assume we have 4 bit integers, and our bound is 3 as you
can see in the widget.

Here's how the distribution follows:

```ts
0: [0, 3, 6, 9, 12, 15]
1: [1, 4, 7, 10, 13]
2: [2, 5, 8, 11, 14]
```

As you can see, we have 6/16 changes to get 0, but only 5/16 chance to get 1 or 2.
There's a 1/16 (0.0625) bias towards generating zeroes. Of course this bias gets lower
and lower as we get larger intervals to pick numbers from, because the denominator gets
greater every time; so at 64 bits, this effect is mostly negligible. However, we still
want to solve it. How? We just keep iterating until we get a random number we like!

<div class="bint-demo">
  <div class="bint-row">
    <label>source bit width
      <select id="bint-bits">
        <option value="4">4 bits (M = 16)</option>
        <option value="8">8 bits (M = 256)</option>
        <option value="16">16 bits (M = 65,536)</option>
        <option value="32">32 bits (M ≈ 4.3·10⁹)</option>
        <option value="64">64 bits (M ≈ 1.8·10¹⁹)</option>
      </select>
    </label>
    <label>bound n
      <input id="bint-n" type="number" min="2" max="100" value="3">
    </label>
    <label>samples
      <input id="bint-samples" type="range" min="1000" max="100000" step="1000" value="20000">
      <span id="bint-samples-val">20000</span>
    </label>
    <button id="bint-roll">re-roll</button>
  </div>
  <div class="bint-row bint-charts">
    <figure>
      <canvas id="bint-mod" width="380" height="220"></canvas>
      <figcaption><code>rand() mod n</code> — pink bars are favored buckets</figcaption>
    </figure>
    <figure>
      <canvas id="bint-rej" width="380" height="220"></canvas>
      <figcaption>rejection sampling — flat within Monte Carlo noise</figcaption>
    </figure>
  </div>
  <p id="bint-info"></p>
</div>

<style>
  .bint-demo { border: 1px solid rgba(127, 127, 127, 0.35); padding: 1em; margin: 1.25em 0; border-radius: 6px; }
  .bint-demo .bint-row { display: flex; flex-wrap: wrap; gap: 0.5em 1em; align-items: center; margin-bottom: 0.75em; }
  .bint-demo label { display: inline-flex; gap: 0.5em; align-items: center; font-size: 0.9em; }
  .bint-demo input[type=range] { width: 10em; }
  .bint-demo input[type=number] { width: 5em; padding: 0.2em 0.4em; }
  .bint-demo button { padding: 0.3em 0.6em; cursor: pointer; font-size: 0.85em; }
  .bint-charts { gap: 1.5em; align-items: flex-start; justify-content: center; }
  .bint-demo figure { margin: 0; text-align: center; }
  .bint-demo figcaption { font-size: 0.8em; opacity: 0.8; margin-top: 0.35em; }
  .bint-demo canvas { background: rgba(127, 127, 127, 0.06); display: block; max-width: 100%; height: auto; }
  #bint-info { font-size: 0.85em; opacity: 0.85; margin: 0.5em 0 0 0; font-family: monospace; }
</style>

<script>
(function () {
  const $ = (id) => document.getElementById(id);
  const modCtx = $('bint-mod').getContext('2d');
  const rejCtx = $('bint-rej').getContext('2d');

  function drawHist(ctx, counts, expected, favoredCount) {
    const w = ctx.canvas.width, h = ctx.canvas.height;
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = 'rgba(127, 127, 127, 0.06)';
    ctx.fillRect(0, 0, w, h);
    const padTop = 12, padBottom = 16;
    const usable = h - padTop - padBottom;
    const n = counts.length;
    const bw = w / n;
    let maxC = 0;
    for (let i = 0; i < n; i++) if (counts[i] > maxC) maxC = counts[i];
    const scaleMax = Math.max(maxC, expected * 1.6);
    for (let i = 0; i < n; i++) {
      ctx.fillStyle = i < favoredCount ? '#D862BC' : '#41C9E2';
      const bh = scaleMax > 0 ? (counts[i] / scaleMax) * usable : 0;
      ctx.fillRect(i * bw + 0.5, h - padBottom - bh, Math.max(bw - 1, 0.5), bh);
    }
    if (expected > 0 && scaleMax > 0) {
      const yE = h - padBottom - (expected / scaleMax) * usable;
      ctx.strokeStyle = 'rgba(127, 127, 127, 0.85)';
      ctx.lineWidth = 1;
      ctx.setLineDash([4, 3]);
      ctx.beginPath();
      ctx.moveTo(0, yE);
      ctx.lineTo(w, yE);
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = 'rgba(127, 127, 127, 0.95)';
      ctx.font = '10px monospace';
      ctx.textBaseline = 'bottom';
      ctx.fillText(`expected ≈ ${expected.toFixed(1)}`, 4, Math.max(yE - 2, padTop + 8));
    }
  }

  function refresh() {
    const bits = parseInt($('bint-bits').value);
    let n = parseInt($('bint-n').value);
    if (!Number.isFinite(n) || n < 2) n = 2;
    if (n > 100) n = 100;
    const samples = parseInt($('bint-samples').value);
    $('bint-samples-val').textContent = samples.toString();

    const modCounts = new Uint32Array(n);
    const rejCounts = new Uint32Array(n);
    let kept = 0;
    let favored, biasResidual, acceptanceRate;

    if (bits <= 32) {
      const M = 2 ** bits;
      if (n > M - 1) n = M - 1;
      const limit = M - (M % n);
      for (let i = 0; i < samples; i++) {
        const r = Math.floor(Math.random() * M);
        modCounts[r % n]++;
        if (r < limit) {
          rejCounts[r % n]++;
          kept++;
        }
      }
      favored = M % n;
      const k = Math.floor(M / n);
      biasResidual = k > 0 ? 1 / k : Infinity;
      acceptanceRate = limit / M;
    } else {
      const M = 1n << 64n;
      const N = BigInt(n);
      const limit = M - (M % N);
      for (let i = 0; i < samples; i++) {
        const hi = BigInt(Math.floor(Math.random() * 2 ** 32));
        const lo = BigInt(Math.floor(Math.random() * 2 ** 32));
        const r = (hi << 32n) | lo;
        const bucket = Number(r % N);
        modCounts[bucket]++;
        if (r < limit) {
          rejCounts[bucket]++;
          kept++;
        }
      }
      favored = Number(M % N);
      biasResidual = n / 2 ** 64;
      acceptanceRate = Number(limit) / Number(M);
    }

    drawHist(modCtx, modCounts, samples / n, favored);
    drawHist(rejCtx, rejCounts, kept / n, 0);

    $('bint-info').textContent =
      `M = 2^${bits} · ${favored} favored / ${n} buckets · ` +
      `bias ≈ 1 + ${biasResidual.toExponential(2)} · ` +
      `rejection acceptance = ${(acceptanceRate * 100).toFixed(4)}%`;
  }

  function syncNBound() {
    const bits = parseInt($('bint-bits').value);
    const maxN = Math.min(100, 2 ** bits - 1);
    const nInput = $('bint-n');
    nInput.max = maxN;
    if (parseInt(nInput.value) > maxN) nInput.value = maxN;
  }

  $('bint-bits').addEventListener('input', () => { syncNBound(); refresh(); });
  $('bint-n').addEventListener('input', refresh);
  $('bint-samples').addEventListener('input', refresh);
  $('bint-roll').addEventListener('click', refresh);
  syncNBound();
  refresh();
})();
</script>

The way "favored" numbers work is for a given sampling space 2^N and a bound `a`, the
numbers `i < 2^N - k * a` where `k * a` is the largest multiple of `a` that is smaller
than or equal to `2^N`. For the simple case of `N=4`, `a=3`, `k` is `5`, so
`i < 2^4 - 5 * 3` gives us only `0`. For any `(N, a)` though, this can never exceed 50%
of all inputs. The effect is largest at `2^(N-1) + 1`, such as `N=4` and `a=9`. Here,
all but 2 numbers within the bound have the bias, and all numbers higher than the bound
within the randomness source "are" the bias. Even in this worst case, it is slightly
less than 50% chance that we'll hit a biased part of the sampling space. So, we can just
reject any biased sampling, and keep sampling with minimal cost here's a an example in
Java
[(taken from)](https://web.archive.org/web/20200520071940/https://www.pcg-random.org/posts/bounded-rands.html):

```java
static uint32_t bounded_rand(rng_t& rng, uint32_t range) {
    uint32_t x, r;
    do {
        x = rng();
        r = x % range;
    } while (x - r > (-range));
    return r;
}
```

Now that we can randomly generate simple types, let's see how we actually use these
building blocks in Property-Based Testing.

## Generating Random Data for Testing Programs

The first thing we need when generating structures is the ability to generate multiple
things, dependently. Well, we could technically just write:

```ts
function genNum(): number {
  let b = randBool(0.5);
  let c = b ? randBounded(0, 10) : randBounded(10, 20);
  return c;
}
```

There's a small issue here, which is that the RNG is hidden. We would ideally like to
have the randomness state around so we can explicitly manipulate it. That's not that
hard, we can just pass the `rng` to every function that uses it:

```ts
function genNum(rng): number {
  let b = randBool(rng, 0.5);
  let c = b ? randBounded(rng, 0, 10) : randBounded(rng, 10, 20);
  return c;
}
```

Another popular technique is (originated from QuickCheck I assume) is to instead have
the generators return a recipe for generation (`Gen<T>`) instead of being functions that
expect an `rng` to compute `T`.

```ts
function getNum(): Gen<number> {
  bind(randBool(0.5), (b) =>
  bind(c ? randBounded(0, 10) : randBounded(10, 20), (c) =>
    (ret c)
  ))
}
```

Then there is another function `sample` of the type `Rng -> Gen<T> -> T` that allows you
to pull out `T` cleanly after producing the generator without needing to thread in the
RNG. Another benefit of this approach is that you generator composition is now hidden
under `bind`, so you can actually do more than just generating random structures. For
instance, you can switch between different sources of randomness and styles of
randomness.

The simplest is using an in-place mutable RNG:

```ts
// c1 mutates rng
type Gen<T> = (rng) => T;

function bind<T1, T2>(c1: Gen<T1>, c2: (T1) => Gen<T2>) {
  return (rng) => {
    const t1 = c1(rng);
    return c2(t1)(rng);
  };
}
```

Using a
[splittable RNG](https://wiki.haskell.org/wikiupload/7/74/Hiw2012-michal-palka.pdf) is
somewhat more safe; they are pure and parallelizable at the cost of being a bit slower.

```ts
type Gen<T> = (rng: Rng) => T;

function bind<T1, T2>(c1: Gen<T1>, c2: (T1) => Gen<T2>): Gen<T2> {
  return (rng) => {
    const [r1, r2] = split(rng);
    return c2(c1(r1))(r2);
  };
}
```

The last popular option is to use a choice buffer or sequence, Hypothesis style:

```ts
type Gen<T> = (buf: ChoiceBuffer) => T;

function bind<T1, T2>(c1: Gen<T1>, c2: (T1) => Gen<T2>): Gen<T2> {
  return (buf) => {
    const t1 = c1(buf);
    return c2(t1)(buf);
  };
}
```

In the randomness buffer approach, each generator moves the cursor along the buffer by
reading a number of random bytes from it; the corollary of which is that you get
_internal shrinking_ and you can use an existing fuzzer to drive your tests. However,
any one of these approaches give you roughly the same capabilities, generate something,
update the RNG state, generate the next thing, and so on... So let's assume we want to
write a list generator, here's what a uniform random list looks like:

```ts
function genList<T>(rng, g: Gen<T>): T[] {
  const len = randPositiveInteger(rng);
  const out = [];
  for (let i = 0; i < len; i++) {
    out.push(g(rng));
  }
  return out;
}
```

The issue here is that however theoretically sound, we do _not_ want uniform lists
distributed over unifornm lengths. There are two competing forces here, one is that
generating and testing small lists are much faster. So we can generate and test 1000
lists of length 10 in the time it takes to generate and test a list of length 10000.
This is coupled with the "small-scope theory" which asserts that many of the bugs we can
find via large test cases also show up for small cases, which is the basis for using
enumerative testing techniques that exhaust the search space from small to large inputs.
Of course, not all bugs emerge at small scales, and exhaustive search is _very_
expensive. We can also couple this fact with another theory, which says that large
inputs exhibit behaviors you would observe in a variety of smaller tests, so generating
and testing one large input can give you more information about the system then `N`
small inputs can.

These competing theories, both of which can be correct in different circumstances, mean
we can to generate both small and large inputs at the same time, and we actually
probably don't want to generate uniformly, we want bias towards specific parts of the
search space. For instance, Hypothesis has `_constant_floats` and `_constant_strings`
that they inject into an otherwise very random set of inputs. (sneak peek):

```python
_constant_floats = (
    [
        ...
        3.402823466e38,
        9007199254740992.0,
        1 - 10e-6,
        2 + 10e-6,
        1.192092896e-07,
        2.2204460492503131e-016,
    ]
    + [2.0**-n for n in (24, 14, 149, 126)]  # minimum (sub)normals for float16,32
    + [float_info.min / n for n in (2, 10, 1000, 100_000)]  # subnormal in float64
)

_constant_strings = {
    ...
    # readable variations on text (bolt/italic/script)
    "𝐓𝐡𝐞 𝐪𝐮𝐢𝐜𝐤 𝐛𝐫𝐨𝐰𝐧 𝐟𝐨𝐱 𝐣𝐮𝐦𝐩𝐬 𝐨𝐯𝐞𝐫 𝐭𝐡𝐞 𝐥𝐚𝐳𝐲 𝐝𝐨𝐠",
    "𝕿𝖍𝖊 𝖖𝖚𝖎𝖈𝖐 𝖇𝖗𝖔𝖜𝖓 𝖋𝖔𝖝 𝖏𝖚𝖒𝖕𝖘 𝖔𝖛𝖊𝖗 𝖙𝖍𝖊 𝖑𝖆𝖟𝖞 𝖉𝖔𝖌",
    "𝑻𝒉𝒆 𝒒𝒖𝒊𝒄𝒌 𝒃𝒓𝒐𝒘𝒏 𝒇𝒐𝒙 𝒋𝒖𝒎𝒑𝒔 𝒐𝒗𝒆𝒓 𝒕𝒉𝒆 𝒍𝒂𝒛𝒚 𝒅𝒐𝒈",
    "𝓣𝓱𝓮 𝓺𝓾𝓲𝓬𝓴 𝓫𝓻𝓸𝔀𝓷 𝓯𝓸𝔁 𝓳𝓾𝓶𝓹𝓼 𝓸𝓿𝓮𝓻 𝓽𝓱𝓮 𝓵𝓪𝔃𝔂 𝓭𝓸𝓰",
    "𝕋𝕙𝕖 𝕢𝕦𝕚𝕔𝕜 𝕓𝕣𝕠𝕨𝕟 𝕗𝕠𝕩 𝕛𝕦𝕞𝕡𝕤 𝕠𝕧𝕖𝕣 𝕥𝕙𝕖 𝕝𝕒𝕫𝕪 𝕕𝕠𝕘",
    # upsidown text
    "ʇǝɯɐ ʇᴉs ɹolop ɯnsdᴉ ɯǝɹo˥",
    # reserved strings in windows
    "NUL",
    "COM1",
    "LPT1",
    # scunthorpe problem
    "Scunthorpe",
    # zalgo text
    "Ṱ̺̺̕o͞ ̷i̲̬͇̪͙n̝̗͕v̟̜̘̦͟o̶̙̰̠kè͚̮̺̪̹̱̤ ̖t̝͕̳̣̻̪͞h̼͓̲̦̳̘̲e͇̣̰̦̬͎ ̢̼̻̱̘h͚͎͙̜̣̲ͅi̦̲̣̰̤v̻͍e̺̭̳̪̰-m̢iͅn̖̺̞̲̯̰d̵̼̟͙̩̼̘̳ ̞̥̱̳̭r̛̗̘e͙p͠r̼̞̻̭̗e̺̠̣͟s̘͇̳͍̝͉e͉̥̯̞̲͚̬͜ǹ̬͎͎̟̖͇̤t͍̬̤͓̼̭͘ͅi̪̱n͠g̴͉ ͏͉ͅc̬̟h͡a̫̻̯͘o̫̟̖͍̙̝͉s̗̦̲.̨̹͈̣",
    #
    ...
}
```

Another typical approach is the use of "size" in biasing. In the case of Hypothesis (as
far as I know), it starts with a small number of small inputs and then promote to
uniform randomness (with the exception of the constants). In the case of QuickCheck, the
size function is a somewhat weird one:

```hs
computeSize :: State -> Int
computeSize MkState{replayStartSize = Just s,numSuccessTests = 0,numRecentlyDiscardedTests=0} = s
-- NOTE: Beware that changing this means you also have to change `prop_discardCoverage` as that currently relies
-- on the sequence produced by this function.
computeSize MkState{maxSuccessTests = ms, maxTestSize = mts, maxDiscardedRatio = md,numSuccessTests=n,numRecentlyDiscardedTests=d}
    -- e.g. with maxSuccess = 250, maxSize = 100, goes like this:
    -- 0, 1, 2, ..., 99, 0, 1, 2, ..., 99, 0, 2, 4, ..., 98.
    | n `roundTo` mts + mts <= ms ||
      n >= ms ||
      ms `mod` mts == 0 = (n `mod` mts + d `div` dDenom) `min` mts
    | otherwise =
      ((n `mod` mts) * mts `div` (ms `mod` mts) + d `div` dDenom) `min` mts
  where
    -- The inverse of the rate at which we increase size as a function of discarded tests
    -- if the discard ratio is high we can afford this to be slow, but if the discard ratio
    -- is low we risk bowing out too early
    dDenom
      | md > 0 = (ms * md `div` 3) `clamp` (1, 10)
      | otherwise = 1 -- Doesn't matter because there will be no discards allowed
    n `roundTo` m = (n `div` m) * m
```

Essentially, size is a counter to number of tests modulo maximum size, with a small edge
case that the last cycle would be incomplete so instead they increase step size to make
it complete too. In QuickChick, or in my other forks, I've usually just used `log2(N)`
with some downward bias to make sure we're not glossing over small inputs
(`log2(16) = 4`, so that means inputs up to size 3 are only tested for 15 inputs, not
great). I don't think PBT literature really agrees on what the right way to do this is,
it's also very hard to decide on what size means too. Here's the issue:

```hs
data Tree = Leaf Int | Node Tree Tree

genTree n :: Int -> Gen Tree
genTree n =
  if n == 0 then
    Leaf <$> arbitrary
  else
    oneof [Leaf <$> arbitrary, Node <$> genTree (n-1) <*> genTree (n-1)]

genTree' n :: Int -> Gen Tree
genTree' n =
  if n == 0 then
    Leaf <$> arbitrary
  else
    oneof [Leaf <$> arbitrary, Node <$> genTree' (n / 2) <*> genTree' (n / 2)]
```

Both of these generators are technically "correct", however the first one treats the
size variable as its depth, while the second treats it as the number of nodes. The
corollary of this is that the trees generated by the first one will be expontentially
larger compared to the second one; they'll be exponentially slower to generate and
execute, and for something like `maxSize = 100`, that slowness will be colossal. Some
frameworks, again such as Hypothesis, or Hedgehog, use a `recursive` combinator that
auto-handles the depth, hiding the sizing from the user. This is probably a good
starting point, but when you think about trees a bit you'll also probably realize
dividing the size `n/2` is not the greatest idea. We'll end up with soo many balanced
trees. Ideally we want right skewed, left skewed, balanced trees that can generate a
variety of behaviors. This also goes back to the idea of
[Swarm Testing](https://dl.acm.org/doi/10.1145/2338965.2336763), where we essentially
want to randomize the choices of randomness, otherwise you'll end up with random-looking
structures, but for instance you'll never end up with a list of all 1's. Will Wilson has
a great Papers We Love talk on this that I will link when it's available online. Another
approach I've seen is to use Boltzmann sampling for diversifying generation.
([1](https://byorgey.wordpress.com/2016/09/20/the-generic-random-library-part-1-simple-generic-arbitrary-instances/),
[2](https://byorgey.wordpress.com/2016/03/23/boltzmann-sampling-for-generic-arbitrary-instances/),
[3](https://julesjacobs.com/misc/treegen/),
[4](https://byorgey.wordpress.com/2013/04/25/random-binary-trees-with-a-size-limited-critical-boltzmann-sampler-2/)).
