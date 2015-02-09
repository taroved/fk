#!/bin/bash

#incons
inconsIP=$(docker inspect --format '{{ .NetworkSettings.IPAddress }}' incons_app)
echo $inconsIP
sed -e "s/_IP_/$inconsIP/g" ./sites-templates/incons.conf.template > ./sites-enabled/incons.conf

#wagtail
#siteIP=$(docker inspect --format '{{ .NetworkSettings.IPAddress }}' sharp_fermat)
#echo $siteIP
#sed -e "s/_IP_/$siteIP/g" ./sites-templates/wagtail-demo.conf.template > ./sites-enabled/wagtail-demo.conf

#gahsc
siteIP=$(docker inspect --format '{{ .NetworkSettings.IPAddress }}' gahsc.net)
echo $siteIP
sed -e "s/_IP_/$siteIP/g" ./sites-templates/gahsc.conf.template > ./sites-enabled/gahsc.conf

#forumkyiv
siteIP=$(docker inspect --format '{{ .NetworkSettings.IPAddress }}' forumkyiv.org)
echo $siteIP
sed -e "s/_IP_/$siteIP/g" ./sites-templates/forumkyiv.conf.template > ./sites-enabled/forumkyiv.conf

docker restart nginx
