> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Recharge and Rate Limiting

To ensure fair distribution of resources and prevent malicious attacks, we currently apply rate limits based on the cumulative recharge amount of each account. The specific limits are shown in the table below. If you have higher requirements, please contact us via email at [api-service@moonshot.ai](mailto:api-service@moonshot.ai).

* To prevent abuse, you need to recharge at least \$1 to start using, and when your cumulative recharge reaches \$5, you will receive a \$5 voucher.

## Explanation of Rate Limits Concepts

* Concurrency: The maximum number of requests from you that we can process at the same time.
* RPM: Requests per minute, which means the maximum number of requests you can send to us in one minute.
* TPM: Tokens per minute, which means the maximum number of tokens you can interact with us in one minute.
* TPD: Tokens per day, which means the maximum number of tokens you can interact with us in one day.

For more details, please refer to the [Rate Limits](/introduction#rate-limits) section.

## Why Do We Implement Rate Limits?

Rate limits are a common practice for API interfaces, and there are several reasons for it:

* They help prevent abuse or misuse of the API. For example, malicious actors might try to overwhelm the API with a large number of requests, attempting to overload it or cause service disruptions. By setting rate limits, we can guard against such behavior.
* Rate limits ensure fair access to the API for everyone. If one person or organization sends too many requests, it could slow down the API for everyone else. By limiting the number of requests a single user can send, we ensure that as many people as possible can use the API without experiencing slowdowns.
* Rate limits help us manage the overall load on our cluster. A sudden surge in requests to the API could put pressure on the servers and lead to performance issues. By setting rate limits, we can maintain a smooth and consistent experience for all users.

## Special Notes

* We will do our best to ensure normal usage for users, but when the cluster load reaches its capacity limit, we may take temporary measures to adjust the rate limits.
* Vouchers do not count towards the cumulative recharge total.
