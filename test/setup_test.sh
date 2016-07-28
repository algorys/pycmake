#!/usr/bin/env bash
#
# Copyright (C) 2016-2016: PyCMake team, actually just Estrada Matthieu
#
# This file is part of PyCMake.
#
# PyCMake is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyCMake is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyCMake.  If not, see <http://www.gnu.org/licenses/>.

set -e

THIS_PATH=$(dirname "$0")
BASE_PATH=$(dirname "$THIS_PATH")

cd $BASE_PATH

echo ' --------- Update and Install packages ... --------- '
sudo apt-get update

echo '--------- Upgrade pip ... --------- '
pip3 install --upgrade pip

# Install prog AND tests requirements :
#echo '--------- Installing application requirements ... --------- '
#pip install -r requirements.txt
echo '--------- Installing application in development mode ... --------- '
pip3 install -e .
echo '--------- Installing tests requirements ... --------- '
pip3 install --upgrade -r test/requirements.txt
