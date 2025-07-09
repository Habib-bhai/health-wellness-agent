| Feature                    | get_system_prompt()                                    | get_all_tools()                                     |
| -------------------------- | -------------------------------------------------------- | ----------------------------------------------------- |
| *Purpose*                | Returns system prompt (instructions) to be sent to model | Returns list of tools currently attached to the agent |
| *Return Type*            | String (usually formatted LLM prompt)                    | List of tool objects                                  |
| *Use Case*               | Debug, audit, replicate agent reasoning                  | Debug, introspect agent capabilities/tools            |
| *Helpful in Production?* | ✅ Useful for tracing model inputs                        | ✅ Useful for introspection, audit, tool management    |