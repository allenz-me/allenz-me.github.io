rm -rf ./docs
python div.py
hugo --minify
echo "notes.allenz.me" >> ./docs/CNAME
git add --all
git commit -m $1
git push -f origin master
echo "Succeed !"
