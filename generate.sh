rm -rf *.py
rm -rf docs/*.md
java -jar openapi-generator-cli.jar generate \
-i http://api.unibee.top/api.sdk.generator.json \
-g python \
-o . \
--git-repo-id unibee-python-client \
--git-user-id UniB-e-e \
-c config.yaml