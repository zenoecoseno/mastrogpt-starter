//--web true
//--param s3_key $S3_SECRET_KEY
function main(args) {
    return {
        statusCode: 200,
        body: {
            authenticated: true,
            s3_key: args.s3_key,
        }
    }
}