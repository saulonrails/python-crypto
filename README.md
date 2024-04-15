<h1>RSA & AES Encrypt / Decrypt</h1>
  <p>Demonstration of how the RSA and AES algorithms work by simple examples in Python. The codes will generate random RSA and AES key-pairs, will encrypt a short message and will decrypt it back to its original form</p>
  <p>
  <h2>Notes</h2>
  <ul>
    <li>Your output will always be different. The algorithm generates different random key-pairs at each execution.</li>
    <li>Even if you encrypt the same message several times with the same public key, you will get different output. This is because the OAEP padding algorithm injects some randomness with the padding.</li>
    <li>If you try to encrypt larger messages, you will get and exception, because the 1024-bit key limits the maximum message length.
Now play with the above code, modify it and run it to learn how RSA works in action.</li>
  </ul>