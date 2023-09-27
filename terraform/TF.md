Some outputs:
```
$ terraform state list
docker_container.nginx
docker_image.nginx
```
```
$ terraform state show docker_image.nginx:
# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99nginx:latest"
    image_id     = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:32da30332506740a2f7c34d5dc70467b7f14ec67d912703568daff790ab3f755"
}

```

```
$ terraform output
container_id = "0ea648bbb005383de4ba97077beadb9f7c93d96d4a882d8c769156fd3b3d1c93"
image_id = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99nginx:latest"

```


## Best Practices

1. **Using required_providers:** Specifying provider sources and versions help maintain consistency and compatibility.

2. **Resource Dependencies:** Using implicit dependencies by referring to another resource's output aids in managing dependencies.

3. **Variables and Outputs:** Using variables with default values, descriptions, and outputs improves user experience and maintainability.

## docker.tf

- Resource dependencies are well-defined, and variables are used with default values and descriptions.

## yandex.tf

- The required Terraform version is specified, and provider zones are explicit for maintainability.
- Folder management and metadata usage aid in easy updates and instance configuration data management.

## github.tf

- The GITHUB_TOKEN environment variable is used for authentication, ensuring better security.
- Branch protection rules and repository access control are set up for enhanced security and collaboration.
- Teams are created and granted access to repositories with specified permissions, promoting better access control and teamwork.