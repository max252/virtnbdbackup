#!/usr/bin/python3
"""
    Copyright (C) 2023 Michael Ablassmeier <abi@grinser.de>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import logging
from typing import BinaryIO
from argparse import Namespace


def get(
    args: Namespace, fileStream, targetFile: str, targetFilePartial: str
) -> BinaryIO:
    """Open target file based on output writer"""
    if args.stdout is True:
        logging.info("Writing data to zip archive.")
        fileStream.open(targetFile)
    else:
        logging.info("Write data to target file: [%s].", targetFilePartial)
        fileStream.open(targetFilePartial)

    return fileStream