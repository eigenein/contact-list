### Notes

* Main app and API are implemented as two apps within **one Django project** for the sake of simplicity.
* Everywhere I use **local-memory caching** for the sake of simplicity.
* I don't care about Python 2.x compatibility.
* Line width (right margin) is larger than 79 characters.
* Images are proxified through API just to enable caching.

### Questions to clarify

* `setup.py` is **missing**.
* CSV file size **is not checked**.
* Image file size **is not checked**.
* Tests are **missing**.

![docs/screenshot.png](Screenshot)
