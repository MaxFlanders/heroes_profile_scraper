### Heroes Profile Scraper
Some scripts that scrape HotS data from heroesprofile.com using the beautifulsoup4 library.

#### How to use
1. Create a new environment (example uses conda).
    ```shell script
    conda create -n hots_scrapers python=3.8
    ```

2. Activate the environment.
    ```shell script
    conda activate hots_scrapers
    ```

3. Install libraries to environment from requirements.txt.
    ```shell script
    pip install -r requirements.txt
    ```

4. Run script.
    ```shell script
   python heroes_profile.py
   # OR
   python icy_veins.py
   ```
   
The functions `get_heroes` and `get_hero_top_5_matchups` scrape
heroesprofile.com urls for specific pieces of data and return
them as a python list. The `__main__` function prints that data
to screen to prove they are working.

Beautiful Soup Tutorial: https://www.youtube.com/watch?v=ng2o98k983k