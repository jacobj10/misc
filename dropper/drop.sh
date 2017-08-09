# !/bin/bash
PREFIX="/tmp/dropzone"
if [ ! -d "$PREFIX" ]; then
  mkdir "$PREFIX"
fi

while read line; do
  wget -P "$PREFIX" "$line";
done <payload.txt

