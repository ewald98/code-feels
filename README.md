# code-feels
A simple tool written in Python with which you can analyze the general view the community has on various topics (most notably, technologies, programming languages).

## Installation


```
git clone --depth=1 https://github.com/twintproject/twint.git
cd twint
pip3 install . -r requirements.txt
pip3 install --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint
```
### Docker
If you intend on using docker, you can get the [image from dockerhub][dh].

## Usage
You can run the python script with various command line arguments (see [GitWiki][wiki] for details). Here's an example:
```
python3 code_feels.py hashtag=python user=onlytestinghere json=test.json
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

[wiki]: <https://github.com/ewald98/code-feels/wiki/Details>
[dh]: <https://hub.docker.com/repository/docker/ewald98/python-code-feels>
