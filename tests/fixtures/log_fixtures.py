# Git log using --raw formatting
COMMIT_LOG = """commit 852f9155dddc7ba011f426c39705b348e9c71277
Author: User Name <user@email.com>
Date:   Thu Apr 20 18:41:49 2017 -0400

    [User] - Checkout - Implement awesome feature A

    :100644 100644 08b473c3d... 8666f9ecc... M      path/to/another/file/client.py
    :100644 100644 3bc5c894a... fbf601b52... M      path/to/file/order.py
    :100644 100644 859e5ea29... 353d5f570... M      path/to/tests/test_client.py
    :100644 100644 4fa9d3d01... c0d492abe... M      path/to/tests/test_order.py"""

MERGE_COMMIT_LOG = """commit 0f9474def18e6e51a546029c114f9571b2743876
Merge: b39577393 0939d3710
Author: Author Name <author@email.com>
Date:   Fri Apr 21 12:27:07 2017 -0300

    Merge pull request #1234 from repo/branch

        Some awesome commit message"""

SAMPLE_LOG = """commit 852f9155dddc7ba011f426c39705b348e9c71277
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
    :100644 100644 4fa9d3d01... c0d492abe... M      path/to/tests/test_order.py"""
