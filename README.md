# code-typing-derby


## Trying it out

A [`run.sh`](./run.sh) utility is provided for quickly building the image and starting a container.

```shell
$ ./run.sh
```

Then, check out [`http://localhost:8000`](http://localhost:8000) to see the website.

To build and run the web application using Docker compose:

```
docker compose up --watch 
```

By default, the image is set up to start the web application. However, a command-line interface is
provided for demonstration purposes as well. 

To run the command-line entrypoint in the container:

```console
$ ./run.sh hello
```
