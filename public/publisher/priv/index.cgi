#!/home/ugrad/24/s2410303/node-v22.13.1-linux-x64/bin/node

const envs = process.env;

const token = envs["HTTP_CF_TURNSTILE_RESPONSE"] || "";

const checkToken = async (token) => {
    const tokenParts = token.split(" ");
    if (tokenParts.length !== 2 || tokenParts[0] !== "Bearer") {
        return false;
    }
    const tokenValue = tokenParts[1];

    const result = await fetch(
        "https://challenges.cloudflare.com/turnstile/v0/siteverify",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                secret: "{secret}",
                response: tokenValue,
            }),
        }
    );

    const outcome = await result.json();

    return outcome.success;
};

const response = async () => {
    if (!(await checkToken(token))) {
        process.stdout.write("Status: 401\r\n");
        process.stdout.write("\r\n");
        return;
    } else {
        process.stdout.write("Status: 200\r\n");
    }

    process.stdout.write("Content-type: application/json\r\n");
    process.stdout.write("Access-Control-Allow-Origin: null\r\n");
    process.stdout.write("Cache-Control: no-store\r\n");
    process.stdout.write("\r\n");
    process.stdout.write(
        JSON.stringify(
            {
                secret: "this is secret",
                realName: "{real_name}",
                realNameKana: "{real_name_kana}",
                mailAddress: "{utid_name}@coins.tsukuba.ac.jp",
                studentId: "{student_id}",
            },
            null,
            4
        ) + "\n"
    );
};

response();
