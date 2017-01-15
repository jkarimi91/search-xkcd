# Search xkcd

Search xkcd is a search engine for [xkcd] comics.

# Installation

From the project directory, create the necessary virtual environment using [conda]

```
conda env create -f environment.yml
source activate xkcd
```

or [pip]

```
pip install -r requirements.txt
```

# Usage

From the project directory, run

```
python manage.py fetch_comics
python manage.py fit_model
python manage.py runserver
```

then visit [http://localhost:8000/search/](http://localhost:8000/search/) with your web browser.

![usage example (gif)][usage gif]

# Credits

Thanks to [xkcd] for the fantastic comics.

# License
This project is licensed under the terms of the [MIT license].

[pip]:
https://pip.pypa.io/en/stable/
[conda]:
http://conda.pydata.org/docs/index.html
[xkcd]:
http://xkcd.com/
[MIT license]:
http://choosealicense.com/licenses/mit/
[usage gif]:
https://cloud.githubusercontent.com/assets/8411317/21945306/62b4e1ec-d98f-11e6-884c-fa27442f953f.gif
