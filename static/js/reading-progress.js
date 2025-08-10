(function(){
  function onScroll(){
    var article = document.querySelector('article');
    if(!article){return;}
    var bar = document.querySelector('#reading-progress .rp-bar');
    if(!bar){return;}
    var rect = article.getBoundingClientRect();
    var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    var articleTop = article.offsetTop;
    var articleHeight = article.scrollHeight;
    var viewportHeight = window.innerHeight;
    var progress = 0;
    if(articleHeight > viewportHeight){
      progress = ((scrollTop - articleTop) / (articleHeight - viewportHeight)) * 100;
      if(progress < 0) progress = 0;
      if(progress > 100) progress = 100;
    } else {
      progress = 100;
    }
    bar.style.width = progress.toFixed(2) + '%';
    bar.parentElement.setAttribute('aria-valuenow', progress.toFixed(0));
  }
  var scheduled = false;
  function schedule(){
    if(!scheduled){
      scheduled = true;
      requestAnimationFrame(function(){
        scheduled = false; onScroll();
      });
    }
  }
  window.addEventListener('scroll', schedule, {passive:true});
  window.addEventListener('resize', schedule);
  document.addEventListener('DOMContentLoaded', onScroll);
})();
