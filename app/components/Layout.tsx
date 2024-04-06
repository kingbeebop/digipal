// components/Layout.tsx

import React, { FC } from 'react';

interface LayoutProps {
  children: React.ReactNode; // Placeholder for any content within the layout
}

const Layout: FC<LayoutProps> = ({ children }) => {
  return (
    <div className="layout"> 
      {/* Header or navigation could go here */}
      <header>
        <h1>Digipal</h1> 
        {/* Navigation links or other header content */}
      </header>

      <main>{children}</main> {/* Content of the page will be rendered here */}

      {/* Footer could go here */}
      <footer>
        <p>© 2024 My Website</p>
      </footer>
    </div>
  );
};

export default Layout;