Tenfins Crawler
=======================
- Run Selenium Chrome in Heroku!

#### The commented code shows running Chrome in development environment
![](https://github.com/maickom88/tenfins_crawler/blob/main/Screen%20Shot%202021-07-10%20at%2002.36.20.png?raw=true)

Where ChromeDriverManager installs all settings and binary
```python
  webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
```
After that I add the line that configures the binary, where I inform that it is taken from an environment variable
```python
   chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
```
Right after I change the ChromeDriverManager instance for one that will also come from an environment variable, these variables will be configured in Heroku
```python
   webdriver.Chrome(
        executable_path=os.environ.get("CHROMEDRIVER_PATH"),
        options=chrome_options
    )
```
Then go up the application for heroku

- Setting up your Heroku to run Selenium
#### In your heroku project navigate to the '⚙ settings' page and click to configure your variables, which you specified in the project.
##### Then add these links in buildpack
![](https://github.com/maickom88/tenfins_crawler/blob/main/Screen%20Shot%202021-07-10%20at%2002.37.45.png?raw=true)
```json
  CHROMEDRIVER_PATH: /app/.chromedriver/bin/chromedriver
  GOOGLE_CHROME_BIN: /app/.apt/usr/bin/google-chrome
```
```cmd
https://github.com/heroku/heroku-buildpack-google-chrome
https://github.com/heroku/heroku-buildpack-chromedriver
```
It turns out that with Heroku, you have to install “Build packages” to get the chrome drivers for Selenium.

### ℹ Heroku has what's called an Ephemeral File System. So every time you push-and-deploy, the previous state vanishes from existence and a brand new one is created somewhere else. That means that everything your application requires to run needs to be housed inside the repository of your application. So, if you have a repo that uses the Selenium Web Driver, then that web driver should be inside your project as well. That said, you can specify buildpacks within your dyno to install dependencies using apt-get. This buildpack lets you do this. I'd use this buildpack to install selenium ChromDriver everytime you deploy your app.


