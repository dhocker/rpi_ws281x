# Build/install the rpi_ws281x package
# ./build.sh [install]
echo Build and install rpi_ws281x package

rm -rf ./build
python ./setup.py build

if [ "$1" == "install" ]; then
    python ./setup.py install
fi
