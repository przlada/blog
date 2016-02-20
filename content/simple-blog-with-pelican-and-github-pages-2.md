Title: Create a simple blog with Python Pelican and Github Pages - Part Two
Date: 2016-01-19 23:59
Category: python
Tags: python, pelican, github

Hey, there!

How has been the python studies? It's going well? What did you learn today? Tell me on comments above :)

Well, let's go to the second part of this tutorial.

On the previous part i teach you how to create your simple blog and run locally, right? Alright, now i will teach you how to host it on Github Pages.

Basically, to have a Pelican blog on Github Pages, you will have a repository named `your-username.github.io` and this repository will have only two branches: `pelican` and `gh-pages`.<br/>
The `pelican` branch will store the pelican files, like: `content`, `theme`, `plugins`, `settings`...<br/>
The `gh-pages` will store the `output` content.

Let's start.

# Login on your Github account
First you need to to login on [Github website](https://github.com).

# Create a new repository
Now you need to create a new repository, but, there is a special thing, the repository name needs to be:
```
your-github-username.github.io
```

On my case, the repository name will be `guilherme-toti.github.io`.

# Start git locally
After you create your repository, you will see a quick setup page, right?
Now, on `console`, go to you blog folder and type:

```
(blog) $ git init
(blog) $ git remote add origin <your_repository_url>
(blog) $ git checkout -b pelican
```

Before we push the changes, let's do a little trick that would save your life, believe me.<br/>
Create a file named `.gitignore`:
```
(blog) $ touch .gitignore
```

Open `.gitignore` and paste this:
```
# Pelican output folder
output
```

This won't commit the `output` folder to branch `pelican` and you will have a cleaner branch :)

Now, continue, running: 
```
(blog) $ git add .
(blog) $ git commit -m "Initial pelican files"
(blog) $ git push origin pelican
```

Let's go step-by-step:<br/>
`$ git init` will start a git repository on this folder<br/>
`$ git remote add origin <your_repository_url>` will add a remote, in this case, your git repository. *The repository url is on github quick setup page*<br/>
`$ git checkout -b pelican` will create and go to branch `pelican`<br/>
`$ git add .` will prepare your files to next commit<br/>
`$ git commit -m "Initial pelican files"` will commit all your changes<br/>
`# git push origin pelican` will push this commit to the branch pelican. 

Now, to publish your content you need the pip module `ghp-import`:
```
(blog) $ pip install ghp-import
```
> Just to remember: It's better to stay on a `virtualenv`. 

After install `ghp-import`, run:
```
(blog) $ make github
```

And there you go! :)

Now just wait some seconds and you can access your awesome blog at `http://your-github-username.github.io`.

Congragulations!! Now you have a pretty cool blog hosted at Github Pages for free! :)

# Quick Tips
Every time you change something or create new content you need to run:
```
(blog) $ git add .
(blog) $ git commit -m "your commit message"
(blog) $ git push origin pelican
(blog) $ make github
```

That's all folks!
