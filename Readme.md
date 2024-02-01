Set up your credentials in the /app/.env file. These credentials will be from your rabbitmq server setup.

```bash
RABBIT_USER=admin
RABBIT_PASS=password
RABBIT_HOST=your.rabbit.ip.address
```

If you make changes to the dockerfile or any configuration involving the build of the image then you need to rebuild the docker image with the following command.This is usually only needed if you are adding dependencies to requirements.txt

```bash
docker build --no-cache -t task-workers .
```

To run the image in development mode with live code reloading then you just have to run:

```bash
sh start-dev.sh
```

This will process all tasks in the broker's queue.
