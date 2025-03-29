export HOME
cd ~/coins-mypage
curl -LO "https://github.com/8128-33550336/coins-mypage/releases/download/$1/public.tar.gz"
curl -LO "https://github.com/8128-33550336/coins-mypage/releases/download/$1/server-scripts.tar.gz"

rm -rf public
tar -xzvf public.tar.gz
rm -rf server-scripts
tar -xzvf server-scripts.tar.gz

rm public.tar.gz
rm server-scripts.tar.gz
