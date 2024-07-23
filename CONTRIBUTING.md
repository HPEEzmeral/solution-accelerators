# Contributions Guide

Thank you for your interest in contributing to the Solution Accelerators repository. This document
provides guidance on how to contribute a new component or resolve issues in existing ones.

## Getting Started

1. Create a GitHub issue to to describe the motivation behind the changes you want to make.
1. Fork the Repository to your own GitHub account.
1. Clone the forked repository to your local machine.

    ```bash
    git clone https://github.com/<your-username>/solution-accelerators.git
    ```

1. Create a new feature branch to house your changes.

    ```bash
    git checkout -b my-feature-branch
    ```

1. Make your changes.

## Submitting Changes

1. Test your changes thoroughly to ensure everything works as expected.
1. Commit your changes.

    ```bash
    git add .
    git commit -m "Introduce feature ..."
    ```

    > Note that each commit message should use the imperative mood.
      For example, use "Introduce feature x" rather than "This commit introduces feature x."

1. Rebase (if necessary) on top of the branch you're targeting. We strive to keep a linear commit
   history.
1. Push your branch to GitHub.

    ```bash
    git push -u origin my-feature-branch
    ```

1. Create a Pull Request (PR) from your forked repository and fill out the PR template.
1. Describe your changes in detail: why you made them, and any additional information that would
   help the reviewers.

## Style Guide

Please adhere to the following style guide for writing tutorials:

1. General notes:
    - Remove all outputs and metadata from Notebooks before committing to avoid versioning issues
      and repository bloat.
    - Use interactive elements in Notebooks to make the tutorial more engaging.
    - Create self-contained components, without external dependencies.
    - Do not include large files in your commits. For example, if a dataset is too large consider
      hosting it elsewhere and pull it at runtime.
    - Include a `requirements.txt` or `environment.yaml` file specifying each dependency and its
      version.
1. Documentation:
    - Use Jupyter Notebooks for documentation whenever possible. Even if you're running a Python
      script. You can use a Notebook to run the script and document what it does at the same time.
    - Include a README file explaining the component's purpose and prerequisites. Add a feature
      image and a conceptual architecture diagram.
    - Avoid passive voice and use second person when writing documentation.
    - Include proper citations and references.
1. Python style guide:
    - Follow the PEP-8 style [guide](https://peps.python.org/pep-0008/).
    - Use docstrings and comments for code documentation.

## Review Process

One of the maintainers will review your pull request and provide feedback. You may be asked to make
changes. You need one approval to merge your PR. Once approved, your pull request will be merged
into the target branch.
