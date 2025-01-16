//--web true
//--kind nodejs:default

function main(arg) {
    const data = {
        services:
        {
            hello: [
                {
                    name: "hello/world",
                    url: "hello/world",
                }
            ]
        }

    };
    return { "body": data };
}
