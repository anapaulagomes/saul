import pytest


@pytest.fixture
def commit_log():
    return """commit 852f9155dddc7ba011f426c39705b348e9c71277
    Author: User Name <user@email.com>
    Date:   Thu Apr 20 18:41:49 2017 -0400

    [User] - Checkout - Implement awesome feature A

    :100644 100644 08b473c3d... 8666f9ecc... M      path/to/another/file/client.py
    :100644 100644 3bc5c894a... fbf601b52... M      path/to/file/order.py
    :100644 100644 859e5ea29... 353d5f570... M      path/to/tests/test_client.py
    :100644 100644 4fa9d3d01... c0d492abe... M      path/to/tests/test_order.py
    """


@pytest.fixture
def merge_commit_log():
    return """commit 0f9474def18e6e51a546029c114f9571b2743876
    Merge: b39577393 0939d3710
    Author: Author Name <author@email.com>
    Date:   Fri Apr 21 12:27:07 2017 -0300

        Merge pull request #1234 from repo/branch

            Some awesome commit message
    """


@pytest.fixture
def sample_log():
    return """commit 852f9155dddc7ba011f426c39705b348e9c71277
    Author: User Name <user@email.com>
    Date:   Thu Apr 20 18:41:49 2017 -0400

        [User] - Checkout - Implement awesome feature A

        :100644 100644 08b473c3d... 8666f9ecc... M      path/to/another/file/client.py
        :100644 100644 3bc5c894a... fbf601b52... M      path/to/file/order.py
        :100644 100644 859e5ea29... 353d5f570... M      path/to/tests/test_client.py
        :100644 100644 4fa9d3d01... c0d492abe... M      path/to/tests/test_order.py

    commit 852f9155dddc7ba011f426c39705b348e9c71277
    Author: User Name <user@email.com>
    Date:   Wed Apr 19 18:41:49 2017 -0400

        [User] - Checkout - Implement awesome feature B

        :100644 100644 08b473c3d... 8666f9ecc... M      path/to/another/file/client.py
        :100644 100644 859e5ea29... 353d5f570... M      path/to/tests/test_client.py

    commit 852f9155dddc7ba011f426c39705b348e9c71277
    Author: User Name <user@email.com>
    Date:   Tue Apr 18 18:41:49 2017 -0400

        [User] - Checkout - Implement awesome feature C

        :100644 100644 3bc5c894a... fbf601b52... M      path/to/file/order.py
        :100644 100644 4fa9d3d01... c0d492abe... M      path/to/tests/test_order.py
    """


@pytest.fixture
def multi_line_log():
    return """
    commit 3241ec2504224ef432893a7e4805935497edab8a
    Author: Joar Wandborg <joar@wandborg.se>
    Date:   Thu Apr 27 14:33:22 2017 +0200
        Use csv.DictReader when parsing wal-e backup-list (#436)
        wal-e outputs in CSV format using the 'excel-tab' dialect: https://github.com/wal-e/wal-e/blob/3164de68527e6ace269a2112291344b18b9ca6c5/wal_e/operator/backup.py#L63
        The ISO date may be written with a space instead of'T' as delimiter between date
        and time, this causes the old parsing to fail.
        :100755 100755 e2b9099... aa36dca... M  patroni/scripts/wale_restore.py
        :100644 100644 7063351... ba3fe65... M  requirements.txt
        :100644 100644 235ab82... 39e9ad3... M  tests/test_wale_restore.py
    """
