
# Remove header and summary section
# <header>
#             <h1 class="p-name">Proje Günlükleri: CVDL(CV Description Language)#1</h1>
#         </header>
#         <section data-field="subtitle" class="p-summary">
#             Merhabalar, Proje Günlükleri konseptinin ilk yazısı olduğu için projenin kendisine girmeden biraz daha
#             serinin konseptinden bahsetmek…
#         </section>



import os

cwd = os.getcwd()
# for filename in os.listdir(cwd):
#     if filename.endswith(".html"):
#         with open(filename, "r", encoding="utf-8") as f:
#             r = f.read()
#             header_start = r.find('<header>')
#             header_end = r.find('</header>') + len('</header>')

#             # Print header
#             if header_start == -1 or header_end == -1:
#                 print(f"Could not find header in {filename}")

#             section_start = r.find('<section data-field="subtitle" class="p-summary">')
#             section_end = r.find("</section>")

#             if section_start == -1 or section_end == -1:
#                 print(f"Could not find section in {filename}")

#             r = r[:header_start] + r[header_end:section_start] + r[section_end:]
#             f.close()

#         with open(filename, "w", encoding="utf-8") as f:
#             f.write(r)

for filename in os.listdir(cwd):
    if filename.endswith(".html"):
        with open(filename, "r", encoding="utf-8") as f:
            r = f.readlines()
            if '</section>' not in r[2]:
                print(f"Could not find section in {filename}")
                f.close()
                continue
            f.close()
        with open(filename, "w", encoding="utf-8") as f:
            f.writelines(r[:2] + r[3:])

        # with open(filename, "w", encoding="utf-8") as f:
        #     f.write(r)