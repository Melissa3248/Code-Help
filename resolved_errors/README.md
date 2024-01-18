# Errors

Cleaning your conda environment (to free up some storage space, remove corrupted files):

```conda clean --all```

```conda clean -p```

Convert a file to a non-Windows encoding:

```dos2unix filename```

CondaVerificationError: The package for python located at /{path/to}/.conda/pkgs/{file}
appears to be corrupted. The path 'lib/python3.6/{some file}'
specified in the package manifest cannot be found.

```conda clean --all```

Change permissions of files that only have read access (no write access):
(chmod 755 allows everyone to read and execute the file, but only the owner and group have write access.)

```chmod 755 /path/to/file```

If GitHub does not allow you to commit with a message, run the following line, type the commit message in the file that opens, and :wq the file:

```git commit -v```

Resolving the Github error: ```remote: error: GH007: Your push would publish a private email address.```

https://stackoverflow.com/questions/43863522/error-your-push-would-publish-a-private-email-address
