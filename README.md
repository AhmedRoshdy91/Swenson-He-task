# Swenson-He-task

•	it's Swenson He task (APIs for coffee machines and custom coffee pods)

•	use python, Django, restframework, sqlite

•	just download the project and run pip install -r requirements.txt or just enable the virtual env

•	run the server by python manage.py runserver

•	use the APIs as explained in the postman collection

•	examples:
URL: http://127.0.0.1:8000/api/get_all_coffee_pods_by_pack_size
send in the body as json { "pack_size": 3 }
________________________________________
URL: http://127.0.0.1:8000/api/get_all_coffee_pods_by_flavor
send in the body as json { "coffee_flavor": "COFFEE_FLAVOR_VANILLA" }
