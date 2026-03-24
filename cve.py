import nvdlib
result = nvdlib.searchCVE( keywordSearch= "Apache 2.4.1")
for cve in result:
    new_msg = f"{cve.id} - {cve.score}"
    for d in cve.descriptions:
        new_msg += f" - {d.value}"
    print(new_msg)