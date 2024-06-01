import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("YermakAleksandr")
    assert user["login"] == "YermakAleksandr"


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user("ivanbob12213213")
    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")
    assert r["total_count"] == 57
    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("become-qa-automobile")
    assert r["total_count"] == 0



@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("s")
    assert r["total_count"] != 0
