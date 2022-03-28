import glob
import os
import pathlib
import tempfile
import patoolib
import zipfile

from . import BaseManufacturer

class PCBWay(BaseManufacturer.Manufacturer):
    NAME = "PCBWay"

    def process(self, path: str):
        path = pathlib.Path(path)

        if path.suffix != ".rar":
            raise Exception("The PCBWay module requires input file to be a RAR archive")

        temp_dir_in = tempfile.TemporaryDirectory()
        temp_dir_out = tempfile.TemporaryDirectory()

        patoolib.extract_archive(path, outdir=temp_dir_in.name)

        files = list(glob.glob(f"{temp_dir_in.name}\\*\\*\\ok\\*"))
        files = [pathlib.Path(file) for file in files]

        if len(files) == 0:
            raise Exception("The PCBWay module couldn't find the required files in the archive")

        files_map = {
            "ts": "top_solder_mask.GTS",
            "to": "top_silkscreen.GTO",
            "tl": "top_layer.GTL",
            "ko": "board_outline.GKO",
            "drl": "drill.DRL",
            "bs": "bottom_solder_mask.GBS",
            "bo": "bottom_silkscreen.GBO",
            "bl": "bottom_layer.GBL",
        }

        out = path.joinpath(path.parent, f"{path.name}-grb.zip")

        with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as zip_f:
            i = 1
            for file in files:
                name = file.stem
                new_name = ""
                if name in files_map:
                    new_name = files_map[name]
                else:
                    new_name = f"unknown_{i}.G{i}"

                print(f"Mapping {file.stem} to {new_name}")
                zip_f.write(str(file), new_name)

        print(out)
