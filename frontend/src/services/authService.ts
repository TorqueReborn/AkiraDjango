export const loginUser = async (username: string, password: string) => {
  // Example API call
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({ success: true, username });
    }, 1000);
  });
};