# AWS docs archive

Copy of AWS docs for offline use.

This repo is setup with scheduled GitHub Actions to automatically download the latest docs from AWS.
The data is stored in branches named after the AWS service and doc type.

> [!TIP]
>
> The data would be converted into [Kapeli Dash]/[Zeal] docsets using [tzing/dashify-aws-docs].
> Visit https://page.tzing.dev/dashify-aws-docs/ if you are looking for the docsets.
>
> [Kapeli Dash]: https://kapeli.com/dash
> [Zeal]: https://zealdocs.org/
> [tzing/dashify-aws-docs]: https://github.com/tzing/dashify-aws-docs

## Data

See the files in these branches:

| Documentation                       | Branch                             |
| ----------------------------------- | ---------------------------------- |
| [CloudFormation User Guide]         | [`docs/cloudformation/user-guide`] |
| [Redshift Database Developer Guide] | [`docs/redshift/developer-guide`]  |

[CloudFormation User Guide]: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html
[Redshift Database Developer Guide]: https://docs.aws.amazon.com/redshift/latest/dg/index.html
[`docs/cloudformation/user-guide`]: https://github.com/tzing/aws-docs-archive/tree/docs/cloudformation/user-guide
[`docs/redshift/developer-guide`]: https://github.com/tzing/aws-docs-archive/tree/docs/redshift/developer-guide
