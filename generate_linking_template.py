"""Script for generating the AnIML linking template"""


import sdRDM


if __name__ == "__main__":
    lib = sdRDM.DataModel.from_markdown("specifications/animl.md")
    lib.generate_linking_template()
