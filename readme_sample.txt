1.  Install virtual wrapper,virtual env and postgres in your system

2. Create a virtual env for this project "mkvirtualenv sparky"

3. Install git and if possible add the SSH also.

4. Clone the repo by "git  clone https://github.com/niyasimonc/Sparky.git". Pull code from master branch.

5. Edit the ~/.virtualenvs/<your-env>/bin/postactivate.Add thefollowing lines
		
	cd /home/niya/Sparky/file_management  #change directory file path
	python manage.py runserver 8000
		
6. Then install the requirments
		pip install -r req.txt
 
7. Create a database in postgres "file_management_db" and role "file_management" in your local postgres with password 'password'.Then run the following command
    python manage.py migrate


 8. And start using by typing:
 		python manage.py runserver