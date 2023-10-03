## ansible-inventory -i inventory/aws_ec2.yaml --list

```
{
    "_meta": {
        "hostvars": {
            ...
    "all": {
        "children": [
            "ungrouped",
            "aws_ec2"
        ]
    },
    "aws_ec2": {
        "hosts": [
            "ec2-18-236-99-42.us-west-2.compute.amazonaws.com",
            "ec2-35-93-48-64.us-west-2.compute.amazonaws.com",
            "ec2-54-185-60-218.us-west-2.compute.amazonaws.com",
            "ec2-52-40-36-253.us-west-2.compute.amazonaws.com"
        ]
    }
}
```




