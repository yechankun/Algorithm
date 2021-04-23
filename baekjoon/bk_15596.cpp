#include <vector>
long sum(std::vector<int> &a) {
	long ans = 0;
    for (auto k:a)
		ans = ans + k;
	return ans;
}
