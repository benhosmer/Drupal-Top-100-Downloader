Drupal-Top-100-Downloader
=========================

The script downloads the current top 100 drupal modules from http://drupal.org/project/usage
It requires drush: http://drupal.org/project/drush
And the BeautifulSoup Library: http://www.crummy.com/software/BeautifulSoup/bs4/doc/

The BeautifulSoup library is packaged with this program, so you don't need to download it unless you want to.

Check out the [Downloads](https://github.com/downloads/benhosmer/Drupal-Top-100-Downloader/drupal-top-100-download.zip) for an OS X app that downloads all of the modules within the application package contents.

After you double-click the application, use finder to "Show Package Contents".
Within this folder open Contents/Resources you will find a folder called drupal-modules. 
This is where the downloaded modules are.

After you install drush, from the command line type:
> python drupal-top-100-download.py

