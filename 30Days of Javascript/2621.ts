async function sleep(millis: number): Promise<void> {
    // set time out but, need to return as a promise
    return new Promise((resolve) => {
        setTimeout(() => resolve(), millis)
    })
}
