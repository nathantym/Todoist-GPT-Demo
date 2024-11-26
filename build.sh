rm -rf package deployment-package.zip

pip install -r requirements.txt -t ./package

cp app.py ./package
cd package
zip -r ../deployment-package.zip .
cd ..
