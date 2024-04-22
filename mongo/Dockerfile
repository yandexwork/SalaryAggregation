FROM mongo
COPY data.json /data.json
CMD mongoimport --username ${USERNAME} --password ${PASSWORD} --uri ${DATABASE_URI} --collection salaries --drop --file /data.json