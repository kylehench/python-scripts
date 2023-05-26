## python batch script
```
python convert_media.py -i [source_folder]
```

## shell batch script
```
sh ffmpeg-batch-convert.sh
```
```
sh "C:\Users\hench\Desktop\h265 batch script testing\ffmpeg-batch-convert.sh"
```

## convert to H.265
Note: The Constant Rate Factor or CRF is an option available in the libx264 encoder to set our desired output quality. (0 - lossless to 51 poorest quality. default 23)
```
ffmpeg -i "MVI_0271 (Will).mov" -vcodec libx265 output9.mp4
```

Can also add ls -Recurse for recursive
```
ls | Where { $_.Extension -eq ".mov" } | ForEach { ffmpeg -i $_.FullName -vcodec libx265 $_.Name.Replace(".MOV", ".mp4") }
```

## DaVinci Resolve
dnxhr codec for resolve compatibility issues:
```
ffmpeg -i input.mov -c:v dnxhd -profile:v dnxhr_hq -pix_fmt yuv422p -c:a aac output.mov
```

## batch script
To run script, type "sh script.sh" in Terminal
```
IFS=$'\n'; set -f
for sourceFile in $(find . -iname "*.MOV")
do
    targetFile="${sourceFile%.*}.mp4"
    ffmpeg -i "$sourceFile" -vcodec libx265 -crf 24 "$targetFile"
done
unset IFS; set +f
```