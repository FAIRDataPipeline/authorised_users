import yaml
import fair.identifiers as fdp_id

_users_yaml = yaml.safe_load(open("authorised_users.yaml"))
if "users" not in _users_yaml:
    raise Exception("Expected key users at top level")
_users = _users_yaml["users"]
for _user in _users:
    print(f"Validating user {_user}")
    _required_keys = ["username", "fullname"]
    for _key in _required_keys:
        print(f"Checking for key {_key}")
        if not _key in _user:
            raise Exception(f"Expected key {_key} in user block")
    if not fdp_id.check_github(_user["username"]):
        raise Exception(f"{_user['username']} is not a valid GitHub user")
    if "orgs" in _user:
        if type(_user["orgs"]) is not list:
            raise Exception(f"Orgs must be an array")
print("Validation Passed")