# fampay

Assignment for the backend engineer intern role. 

Note: You might need to update keys.txt with your own keys.

## Usage

To use, make sure you have docker-compose installed and then run the instruction

We need to open up three terminals follow the steps:
1. In the first terminal, execute
`docker-compose up db
`
2. In the second terminal, execute
`docker-compose up web
`
3. In the third terminal, we need to run the migrations to the db.

Run `docker ps
` to identify the container_id of web docker.

After obtaining the id, run `sudo docker exec -t -i <container_id> bash`.
Once the bash shell opens up, run `python manage.py migrate`

After this, you should be able to make calls on postman and get details of videos.
## Known issues

- [ ] getting the error, `django.db.utils.DataError: value too long for type character varying(100)`. Once this error is met, database is not getting populated anymore. Need to implement exception handling.
- [ ]  Currently, not checking whether a video already exists in the db causing duplication error.

## Screenshots

GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
![alt text](https://github.com/ParthS28/fampay/blob/main/images/screenshot2.png "get videos")

A basic search API to search the stored videos using their title and description.

GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
![alt text](https://github.com/ParthS28/fampay/blob/main/images/screenshot3.png "get videos")


![alt text](https://github.com/ParthS28/fampay/blob/main/images/screenshot4.png "get videos")

Optimise search api, so that it's able to search videos containing partial match for the search query in either video title or description.

![alt text](https://github.com/ParthS28/fampay/blob/main/images/screenshot5.png "get videos")


![alt text](https://github.com/ParthS28/fampay/blob/main/images/screenshot6.png "get videos")
