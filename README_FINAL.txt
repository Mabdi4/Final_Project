Modules you might have to install:

python -m pip install pandas
python -m pip install selenium

---------------------------------------

Need to download chrome driver for your specific operating system.

https://chromedriver.storage.googleapis.com/index.html?path=87.0.4280.88/

For Windows place the exe in  C:\Windows, for other operating systems I'm not sure, but for all you can use:

self.driver = webdriver.Chrome(executable_path="path/to/chromedriver.exe") replacing with acutal path.
----------------------------------------------------------------------------------------------------------------
When running the program it was ask you to input number of pages to scrape. Simply put a number like "1" and press enter.

After it is done two csv files will be created called target_tv_dataset.csv and bestbuy_tv_dataset.csv
Move, Rename, or delete the files before running again.
