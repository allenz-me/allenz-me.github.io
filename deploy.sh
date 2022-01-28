# 一般情况下都没有 docs 文件夹

commit_id=`git log -1 --pretty=format:%h`
python div.py
hugo --minify
echo "notes.allenz.me" >> ./docs/CNAME
git add --all
git commit -m $1
git push -f origin master
# echo "Succeed !"
git reset --hard $commit_id