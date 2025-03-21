### Requirements
```bash
brew install orbstack
brew install --cask xquartz
# java JVM (aarch64) https://download.oracle.com/java/24/latest/jdk-24_macos-aarch64_bin.dmg
```

### Setup
```bash
xhost +local:docker
export DISPLAY=host.docker.internal:0
```

### Usage
```bash
# running NS2
chmod +x NSG2.1.jar
java -jar NSG2.1.jar

# Building the image
docker build . -t nam --platform linux/amd64

# Start a temporary container
sudo docker run -it --rm --network host -e DISPLAY=$DISPLAY -v "$PWD":/tmp --platform linux/amd64 nam

# within the vm
root@orbstack# cd /tmp/example
root@orbstack# ns test.tcl
```
