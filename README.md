### Notes and assumptions

* Main app and API are implemented as two apps (`app` and `api`) within **one Django project**.
* I didn't implement paging.
* Everywhere I use **local-memory caching**.
* I don't care about Python 2.x compatibility.
* Line width (right margin) is not strictly limited.
* Images are proxified through API just to enable caching and/or ability to replace the source.

### Questions to clarify

* `setup.py` and other deployment things are **missing**.
* CSV file size **is not checked**.
* Image file size **is not checked**.
* Tests are **missing**.

![Screenshot](docs/screenshot.png)
