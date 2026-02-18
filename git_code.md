#First time setup                                                       #undo staged change
git config --global user.name "RohanBisht33"                            git restore --staged file.py
git config --global user.email "bishtrohan33@gmail.com"                  
git config --global init.defaultBranch main                             #undo local change
                                                                        git restore file.py
#If repo is made explicitly 
git remote add origin https://github.com/RohanBisht33/ML.git            #Undo last commit
git push -u origin main                                                 git reset --soft HEAD~1

#Basic Commands                                                         #tagging and pushing good commits
git status                                                              git tag tag_name
git add .                                                               git push origin tag_name
git commit -m "train cnn v1"
git push                                                                #view and switch tags(readonly)
                                                                        git tag
#Create a branch                                                        git checkout tag_name
git checkout -b exp-resnet50

#switch branches
git checkout main

#list branches
git branch

#remove branches
git branch -d exp-resnet50

#pulling changes in teams
git pull

#Create a venv
cd 
python3 -m venv ~/venv-name

#Activating venv
cd
source ~/venv-name/bin/activate

#Install jupyterkernel inside venv

pip install ipykernel notebook
python -m ipykernel install --user \
  --name venv-name \
  --display-name "Python (venv-name)"
