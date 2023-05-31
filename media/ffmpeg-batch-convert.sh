IFS=$'\n'; set -f
for sourceFile in $(find . -iname "*.MOV")
do
    targetFile="${sourceFile%.*}.mp4"
    ffmpeg -i "$sourceFile" -vcodec libx265 -crf 24 "$targetFile"
done
unset IFS; set +f