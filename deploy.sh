rm -rf ./docs
python div.py
hugo --minify
git add --all
git commit -m $1
git push origin master
echo "Succeed !"
